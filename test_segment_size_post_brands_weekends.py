import unittest
from framework.helpers.segment_size_helper import *
from framework.helpers.segment_size_helper import data_provider
from config import *
import logging

logger = logging.getLogger("cab.tests.segmentSizePostBrandsWeekendTests")

class SegmentSizePostBrandsWeekendTests(unittest.TestCase):

     cnx = None

     ################################### Brand Combination - freq-(1,5,10),duration(all combs), timeofday-morning, dayofweek-weekend ######################################

     freq = lambda: ((1,),(5,),(10,))
     @data_provider(freq)
     def test_user_visit_kfc_of_freq_x_in_last_6_months_on_weekend_morning(self,fre):

        logger.info("Find users who visited kfc "+str(fre)+"times in last 6 months and on weekend and on mornings")

        request = {
            "brand": {"direct": [brand_id+"|"+str(fre)+"|6m|1|2"]}
        }

        segment_size_post(None, request, db_validation=True)

     @data_provider(freq)
     def test_user_visit_kfc_of_freq_x_in_last_month_on_weekend_morning(self,fre):

        logger.info("Find users who visited kfc "+str(fre)+"times in last month and on weekend and on mornings")
        request = {
            "brand": {"direct": [brand_id+"|"+str(fre)+"|1m|1|2"]}

        }

        segment_size_post(None, request, db_validation=True)

     @data_provider(freq)
     def test_user_visit_kfc_of_fre_x_in_last_1_year_on_weekend_morning(self,fre):

        logger.info("Find users who visited kfc "+str(fre)+"times in last 1 year and on weekend and on mornings")
        request = {
            "brand": {"direct": [brand_id+"|"+str(fre)+"|1y|1|2"]}

        }

        segment_size_post(None, request, db_validation=True)

     @data_provider(freq)
     def test_user_visit_kfc_of_freq_x_in_last_quarter_on_weekend_morning(self,fre):

        logger.info("Find users who visited kfc "+str(fre)+"times in last quarter and on weekend and on mornings")
        request = {
            "brand": {"direct": [brand_id+"|"+str(fre)+"|1q|1|2"]}

        }

        segment_size_post(None, request, db_validation=True)


     ################################### Brand Combination - freq-(1,5,10),duration(all combs), timeofday-afternoon, dayofweek-weekend ######################################

     @data_provider(freq)
     def test_user_visit_kfc_of_freq_x_in_last_6_months_on_weekend_afternoon(self,fre):

        logger.info("Find users who visited kfc "+str(fre)+"times in last 6 months and on weekend and on afternoon")

        request = {
            "brand": {"direct": [brand_id+"|"+str(fre)+"|6m|2|2"]}

        }

        segment_size_post(None, request, db_validation=True)

     @data_provider(freq)
     def test_user_visit_kfc_of_freq_x_in_last_month_on_weekend_afternoon(self,fre):

        logger.info("Find users who visited kfc "+str(fre)+"times in last month and on weekend and on afternoon")
        request = {
            "brand": {"direct": [brand_id+"|"+str(fre)+"|1m|2|2"]}

        }

        segment_size_post(None, request, db_validation=True)

     @data_provider(freq)
     def test_user_visit_kfc_of_fre_x_in_last_1_year_on_weekend_afternoon(self,fre):

        logger.info("Find users who visited kfc "+str(fre)+"times in last 1 year and on weekend and on afternoon")
        request = {
            "brand": {"direct": [brand_id+"|"+str(fre)+"|1y|2|2"]}

        }

        segment_size_post(None, request, db_validation=True)

     @data_provider(freq)
     def test_user_visit_kfc_of_freq_x_in_last_quarter_on_weekend_afternoon(self,fre):

        logger.info("Find users who visited kfc "+str(fre)+"times in last quarter and on weekend and on afternoon")
        request = {
            "brand": {"direct": [brand_id+"|"+str(fre)+"|1q|2|2"]}

        }

        segment_size_post(None, request, db_validation=True)


     ################################### Brand Combination - freq-(1,5,10),duration(all combs), timeofday-evening, dayofweek-weekend ######################################

     @data_provider(freq)
     def test_user_visit_kfc_of_freq_x_in_last_6_months_on_weekend_evening(self,fre):

        logger.info("Find users who visited kfc "+str(fre)+"times in last 6 months and on weekend and on evening")

        request = {
            "brand": {"direct": [brand_id+"|"+str(fre)+"|6m|3|2"]}

        }

        segment_size_post(None, request, db_validation=True)

     @data_provider(freq)
     def test_user_visit_kfc_of_freq_x_in_last_month_on_weekend_evening(self,fre):

        logger.info("Find users who visited kfc "+str(fre)+"times in last month and on weekend and on evening")
        request = {
            "brand": {"direct": [brand_id+"|"+str(fre)+"|1m|3|2"]}

        }

        segment_size_post(None, request, db_validation=True)

     @data_provider(freq)
     def test_user_visit_kfc_of_fre_x_in_last_1_year_on_weekend_evening(self,fre):

        logger.info("Find users who visited kfc "+str(fre)+"times in last 1 year and on weekend and on evening")
        request = {
            "brand": {"direct": [brand_id+"|"+str(fre)+"|1y|3|2"]}

        }

        segment_size_post(None, request, db_validation=True)

     @data_provider(freq)
     def test_user_visit_kfc_of_freq_x_in_last_quarter_on_weekend_evening(self,fre):

        logger.info("Find users who visited kfc "+str(fre)+"times in last quarter and on weekend and on evening")
        request = {
            "brand": {"direct": [brand_id+"|"+str(fre)+"|1q|3|2"]}

        }

        segment_size_post(None, request, db_validation=True)


     ################################### Brand Combination - freq-(1,5,10),duration(all combs), timeofday-night, dayofweek-weekend ######################################

     @data_provider(freq)
     def test_user_visit_kfc_of_freq_x_in_last_6_months_on_weekend_night(self,fre):

        logger.info("Find users who visited kfc "+str(fre)+"times in last 6 months and on weekend and on night")

        request = {
            "brand": {"direct": [brand_id+"|"+str(fre)+"|6m|4|2"]}

        }

        segment_size_post(None, request, db_validation=True)

     @data_provider(freq)
     def test_user_visit_kfc_of_freq_x_in_last_month_on_weekend_night(self,fre):

        logger.info("Find users who visited kfc "+str(fre)+"times in last month and on weekend and on night")
        request = {
            "brand": {"direct": [brand_id+"|"+str(fre)+"|1m|4|2"]}

        }

        segment_size_post(None, request, db_validation=True)

     @data_provider(freq)
     def test_user_visit_kfc_of_fre_x_in_last_1_year_on_weekend_night(self,fre):

        logger.info("Find users who visited kfc "+str(fre)+"times in last 1 year and on weekend and on night")
        request = {
            "brand": {"direct": [brand_id+"|"+str(fre)+"|1y|4|2"]}

        }

        segment_size_post(None, request, db_validation=True)

     @data_provider(freq)
     def test_user_visit_kfc_of_freq_x_in_last_quarter_on_weekend_night(self,fre):

        logger.info("Find users who visited kfc "+str(fre)+"times in last quarter and on weekend and on night")
        request = {
            "brand": {"direct": [brand_id+"|"+str(fre)+"|1q|4|2"]}

        }

        segment_size_post(None, request, db_validation=True)

if __name__ == '__main__':
    unittest.main()
