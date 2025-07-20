def predict(url):
	preds = "predicted output"

	return preds
	
def lambda_handler(event, context):
	url = event['url']
	result = predict(url)
	return result

