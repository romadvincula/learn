from pyspark import SparkConf, SparkContext


# find total amount spent by each customer in customer-orders.csv

conf = SparkConf().setMaster("local").setAppName("CustomerSpend")
sc = SparkContext(conf=conf)

def parseLine(line):
    # split each line into fields
    fields = line.split(',')
    # map each line to key-value pairs customer id and dollar spend
    customer = int(fields[0])
    spend = round(float(fields[2]), 2)

    return (customer, spend)

lines = sc.textFile("data/customer-orders.csv")
customerSpends = lines.map(parseLine)

# use reduceByKey to add up amount spend by customer id
spendByCustomer = customerSpends.reduceByKey(lambda x, y: x + y)

# reverse key-value to value-key then run sortbykey on new key
customerSpendSorted = spendByCustomer.map(lambda x: (x[1], x[0]) ).sortByKey()

# collect results and print
results = customerSpendSorted.collect()
for i in results:
    print(i[1], "{:.2f}".format(i[0]))