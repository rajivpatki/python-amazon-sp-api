# coding: utf-8

"""
    Selling Partner API for Pricing

    The Selling Partner API for Pricing helps you programmatically retrieve product pricing and offer information for Amazon Marketplace products.  # noqa: E501

    OpenAPI spec version: v0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class SalesRankType(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'product_category_id': 'str',
        'rank': 'int'
    }

    attribute_map = {
        'product_category_id': 'ProductCategoryId',
        'rank': 'Rank'
    }

    def __init__(self, product_category_id=None, rank=None):  # noqa: E501
        """SalesRankType - a model defined in Swagger"""  # noqa: E501
        self._product_category_id = None
        self._rank = None
        self.discriminator = None
        self.product_category_id = product_category_id
        self.rank = rank

    @property
    def product_category_id(self):
        """Gets the product_category_id of this SalesRankType.  # noqa: E501

         Identifies the item category from which the sales rank is taken.  # noqa: E501

        :return: The product_category_id of this SalesRankType.  # noqa: E501
        :rtype: str
        """
        return self._product_category_id

    @product_category_id.setter
    def product_category_id(self, product_category_id):
        """Sets the product_category_id of this SalesRankType.

         Identifies the item category from which the sales rank is taken.  # noqa: E501

        :param product_category_id: The product_category_id of this SalesRankType.  # noqa: E501
        :type: str
        """
        if product_category_id is None:
            raise ValueError("Invalid value for `product_category_id`, must not be `None`")  # noqa: E501

        self._product_category_id = product_category_id

    @property
    def rank(self):
        """Gets the rank of this SalesRankType.  # noqa: E501

        The sales rank of the item within the item category.  # noqa: E501

        :return: The rank of this SalesRankType.  # noqa: E501
        :rtype: int
        """
        return self._rank

    @rank.setter
    def rank(self, rank):
        """Sets the rank of this SalesRankType.

        The sales rank of the item within the item category.  # noqa: E501

        :param rank: The rank of this SalesRankType.  # noqa: E501
        :type: int
        """
        if rank is None:
            raise ValueError("Invalid value for `rank`, must not be `None`")  # noqa: E501

        self._rank = rank

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(SalesRankType, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SalesRankType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
