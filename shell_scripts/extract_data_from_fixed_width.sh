cut -b 59- /home/test/Imp/Kafka-airflow/payment-data.txt > /home/test/Imp/Kafka-airflow/fixed_width.txt
tr " " "," < /home/test/Imp/Kafka-airflow/fixed_width.txt > /home/test/Imp/Kafka-airflow/fixed_width_data.csv
