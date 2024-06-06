service_account_mail=$1
key_file=$2

gcloud auth activate-service-account "$service_account_mail" --key-file "$key_file"
