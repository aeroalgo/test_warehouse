from django.db import connection
from django.core.management import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **options):
        connection.ensure_connection()
        try:
            with connection.cursor() as cursor:
                query = """
                INSERT INTO accounting_product (article) VALUES (%s);
                INSERT INTO accounting_product (article) VALUES (%s);
                INSERT INTO accounting_product (article) VALUES (%s);
                INSERT INTO accounting_product (article) VALUES (%s);
                """

                data = ["1000001", "1000002", "1000003", "1000004"]
                cursor.execute(query, data)
                sku1 = """(SELECT id from accounting_product WHERE article='1000001')"""
                sku2 = """(SELECT id from accounting_product WHERE article='1000002')"""
                sku3 = """(SELECT id from accounting_product WHERE article='1000003')"""
                sku4 = """(SELECT id from accounting_product WHERE article='1000004')"""
                query = f"""
                INSERT INTO accounting_storage (sku_id, count, actual_date) VALUES ({sku1},500,'2022-12-12 00:00:00');
                INSERT INTO accounting_storage (sku_id, count, actual_date) VALUES ({sku2},400,'2022-12-12 00:00:00');
                INSERT INTO accounting_storage (sku_id, count, actual_date) VALUES ({sku3},553,'2022-12-12 00:00:00');
                INSERT INTO accounting_storage (sku_id, count, actual_date) VALUES ({sku4},110,'2022-12-12 00:00:00');
                INSERT INTO accounting_storage (sku_id, count, actual_date) VALUES ({sku1},497,'2022-12-12 03:00:00');
                INSERT INTO accounting_storage (sku_id, count, actual_date) VALUES ({sku2},395,'2022-12-12 03:00:00');
                INSERT INTO accounting_storage (sku_id, count, actual_date) VALUES ({sku3},552,'2022-12-12 03:00:00');
                INSERT INTO accounting_storage (sku_id, count, actual_date) VALUES ({sku4},109,'2022-12-12 03:00:00');
                INSERT INTO accounting_storage (sku_id, count, actual_date) VALUES ({sku1},491,'2022-12-12 06:00:00');
                INSERT INTO accounting_storage (sku_id, count, actual_date) VALUES ({sku2},385,'2022-12-12 06:00:00');
                INSERT INTO accounting_storage (sku_id, count, actual_date) VALUES ({sku3},550,'2022-12-12 06:00:00');
                INSERT INTO accounting_storage (sku_id, count, actual_date) VALUES ({sku4},107,'2022-12-12 06:00:00');
                INSERT INTO accounting_storage (sku_id, count, actual_date) VALUES ({sku1},482,'2022-12-12 09:00:00');
                INSERT INTO accounting_storage (sku_id, count, actual_date) VALUES ({sku2},370,'2022-12-12 09:00:00');
                INSERT INTO accounting_storage (sku_id, count, actual_date) VALUES ({sku3},547,'2022-12-12 09:00:00');
                INSERT INTO accounting_storage (sku_id, count, actual_date) VALUES ({sku4},104,'2022-12-12 09:00:00');
                INSERT INTO accounting_storage (sku_id, count, actual_date) VALUES ({sku1},470,'2022-12-12 12:00:00');
                INSERT INTO accounting_storage (sku_id, count, actual_date) VALUES ({sku2},350,'2022-12-12 12:00:00');
                INSERT INTO accounting_storage (sku_id, count, actual_date) VALUES ({sku3},543,'2022-12-12 12:00:00');
                INSERT INTO accounting_storage (sku_id, count, actual_date) VALUES ({sku4},100,'2022-12-12 12:00:00');
                INSERT INTO accounting_storage (sku_id, count, actual_date) VALUES ({sku1},455,'2022-12-12 15:00:00');
                INSERT INTO accounting_storage (sku_id, count, actual_date) VALUES ({sku2},325,'2022-12-12 15:00:00');
                INSERT INTO accounting_storage (sku_id, count, actual_date) VALUES ({sku3},538,'2022-12-12 15:00:00');
                INSERT INTO accounting_storage (sku_id, count, actual_date) VALUES ({sku4},95,'2022-12-12 15:00:00');
                INSERT INTO accounting_storage (sku_id, count, actual_date) VALUES ({sku1},437,'2022-12-12 18:00:00');
                INSERT INTO accounting_storage (sku_id, count, actual_date) VALUES ({sku2},295,'2022-12-12 18:00:00');
                INSERT INTO accounting_storage (sku_id, count, actual_date) VALUES ({sku3},532,'2022-12-12 18:00:00');
                INSERT INTO accounting_storage (sku_id, count, actual_date) VALUES ({sku4},89,'2022-12-12 18:00:00');
                INSERT INTO accounting_storage (sku_id, count, actual_date) VALUES ({sku1},416,'2022-12-12 21:00:00');
                INSERT INTO accounting_storage (sku_id, count, actual_date) VALUES ({sku2},260,'2022-12-12 21:00:00');
                INSERT INTO accounting_storage (sku_id, count, actual_date) VALUES ({sku3},525,'2022-12-12 21:00:00');
                INSERT INTO accounting_storage (sku_id, count, actual_date) VALUES ({sku4},82,'2022-12-12 21:00:00');
                INSERT INTO accounting_storage (sku_id, count, actual_date) VALUES ({sku1},392,'2022-12-13 00:00:00');
                INSERT INTO accounting_storage (sku_id, count, actual_date) VALUES ({sku2},220,'2022-12-13 00:00:00');
                INSERT INTO accounting_storage (sku_id, count, actual_date) VALUES ({sku3},517,'2022-12-13 00:00:00');
                INSERT INTO accounting_storage (sku_id, count, actual_date) VALUES ({sku4},74,'2022-12-13 00:00:00');
                INSERT INTO accounting_storage (sku_id, count, actual_date) VALUES ({sku1},365,'2022-12-13 03:00:00');
                INSERT INTO accounting_storage (sku_id, count, actual_date) VALUES ({sku2},175,'2022-12-13 03:00:00');
                INSERT INTO accounting_storage (sku_id, count, actual_date) VALUES ({sku3},508,'2022-12-13 03:00:00');
                INSERT INTO accounting_storage (sku_id, count, actual_date) VALUES ({sku4},65,'2022-12-13 03:00:00');
                INSERT INTO accounting_storage (sku_id, count, actual_date) VALUES ({sku1},335,'2022-12-13 06:00:00');
                INSERT INTO accounting_storage (sku_id, count, actual_date) VALUES ({sku2},125,'2022-12-13 06:00:00');
                INSERT INTO accounting_storage (sku_id, count, actual_date) VALUES ({sku3},498,'2022-12-13 06:00:00');
                INSERT INTO accounting_storage (sku_id, count, actual_date) VALUES ({sku4},55,'2022-12-13 06:00:00');
                INSERT INTO accounting_storage (sku_id, count, actual_date) VALUES ({sku1},302,'2022-12-13 09:00:00');
                INSERT INTO accounting_storage (sku_id, count, actual_date) VALUES ({sku2},500,'2022-12-13 09:00:00');
                INSERT INTO accounting_storage (sku_id, count, actual_date) VALUES ({sku3},487,'2022-12-13 09:00:00');
                INSERT INTO accounting_storage (sku_id, count, actual_date) VALUES ({sku4},44,'2022-12-13 09:00:00');
                INSERT INTO accounting_storage (sku_id, count, actual_date) VALUES ({sku1},266,'2022-12-13 12:00:00');
                INSERT INTO accounting_storage (sku_id, count, actual_date) VALUES ({sku2},440,'2022-12-13 12:00:00');
                INSERT INTO accounting_storage (sku_id, count, actual_date) VALUES ({sku3},475,'2022-12-13 12:00:00');
                INSERT INTO accounting_storage (sku_id, count, actual_date) VALUES ({sku4},32,'2022-12-13 12:00:00');
                INSERT INTO accounting_storage (sku_id, count, actual_date) VALUES ({sku1},227,'2022-12-13 15:00:00');
                INSERT INTO accounting_storage (sku_id, count, actual_date) VALUES ({sku2},375,'2022-12-13 15:00:00');
                INSERT INTO accounting_storage (sku_id, count, actual_date) VALUES ({sku3},462,'2022-12-13 15:00:00');
                INSERT INTO accounting_storage (sku_id, count, actual_date) VALUES ({sku4},19,'2022-12-13 15:00:00');
                INSERT INTO accounting_storage (sku_id, count, actual_date) VALUES ({sku1},185,'2022-12-13 18:00:00');
                INSERT INTO accounting_storage (sku_id, count, actual_date) VALUES ({sku2},305,'2022-12-13 18:00:00');
                INSERT INTO accounting_storage (sku_id, count, actual_date) VALUES ({sku3},448,'2022-12-13 18:00:00');
                """
                cursor.execute(query)
        except Exception as e:
            print("Данные уже есть в базе")
