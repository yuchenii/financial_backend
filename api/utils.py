# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/6/22 14:56
# @Author  : yuchen
# @File    : utils.py
# @Software: PyCharm

from models.financial_product import FinancialProductModel
from models.fund import FundModel
from models.insurance import InsuranceModel


def get_product_info(product_id, product_type):
    """
    获取产品信息
    :param product_id:产品ID
    :param product_type:产品类型
    :return:产品信息
    """
    product_info = ""
    if product_type == 0:
        product_info = FinancialProductModel.find_by_id(product_id)
    elif product_type == 1:
        product_info = InsuranceModel.find_by_id(product_id)
    elif product_type == 2:
        product_info = FundModel.find_by_id(product_id)

    if not product_info:
        return ""
    return product_info.json()


def paging_query(model, page_index, page_size):
    """
    分页查询
    :param model:模型
    :param page_index:页码
    :param page_size:页大小
    :return:分页结果
    """
    total_count = model.query.count()
    total_page = (total_count + page_size - 1) // page_size
    if page_index > total_page:
        page_index = total_page
    if page_index < 1:
        page_index = 1
    start = (page_index - 1) * page_size
    end = start + page_size
    return model.query.slice(start, end), page_index, total_page, total_count
