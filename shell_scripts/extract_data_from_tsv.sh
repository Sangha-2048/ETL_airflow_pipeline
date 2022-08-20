cut -f5,6,7 /home/test/Imp/Kafka-airflow/tollplaza-data.tsv > /home/test/Imp/Kafka-airflow/tcsv_data.tsv
tr $"\t" "," < /home/test/Imp/Kafka-airflow/tcsv_data.tsv > /home/test/Imp/Kafka-airflow/partial_res.csv 
tr -d $"\r" < /home/test/Imp/Kafka-airflow/partial_res.csv > /home/test/Imp/Kafka-airflow/tcsv_data.csv
