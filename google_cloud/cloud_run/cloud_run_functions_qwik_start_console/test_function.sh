curl -X POST "https://gcfunction-hello-809134197254.australia-southeast1.run.app" \
-H "Authorization: bearer $(gcloud auth print-identity-token)" \
-H "Content-Type: application/json" \
-d '{"name": "Developer"}'