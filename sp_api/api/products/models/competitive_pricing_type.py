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


class CompetitivePricingType(object):
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
        'competitive_prices': 'CompetitivePriceList',
        'number_of_offer_listings': 'NumberOfOfferListingsList',
        'trade_in_value': 'MoneyType'
    }

    attribute_map = {
        'competitive_prices': 'CompetitivePrices',
        'number_of_offer_listings': 'NumberOfOfferListings',
        'trade_in_value': 'TradeInValue'
    }

    def __init__(self, competitive_prices=None, number_of_offer_listings=None, trade_in_value=None):  # noqa: E501
        """CompetitivePricingType - a model defined in Swagger"""  # noqa: E501
        self._competitive_prices = None
        self._number_of_offer_listings = None
        self._trade_in_value = None
        self.discriminator = None
        self.competitive_prices = competitive_prices
        self.number_of_offer_listings = number_of_offer_listings
        if trade_in_value is not None:
            self.trade_in_value = trade_in_value

    @property
    def competitive_prices(self):
        """Gets the competitive_prices of this CompetitivePricingType.  # noqa: E501


        :return: The competitive_prices of this CompetitivePricingType.  # noqa: E501
        :rtype: CompetitivePriceList
        """
        return self._competitive_prices

    @competitive_prices.setter
    def competitive_prices(self, competitive_prices):
        """Sets the competitive_prices of this CompetitivePricingType.


        :param competitive_prices: The competitive_prices of this CompetitivePricingType.  # noqa: E501
        :type: CompetitivePriceList
        """
        if competitive_prices is None:
            raise ValueError("Invalid value for `competitive_prices`, must not be `None`")  # noqa: E501

        self._competitive_prices = competitive_prices

    @property
    def number_of_offer_listings(self):
        """Gets the number_of_offer_listings of this CompetitivePricingType.  # noqa: E501


        :return: The number_of_offer_listings of this CompetitivePricingType.  # noqa: E501
        :rtype: NumberOfOfferListingsList
        """
        return self._number_of_offer_listings

    @number_of_offer_listings.setter
    def number_of_offer_listings(self, number_of_offer_listings):
        """Sets the number_of_offer_listings of this CompetitivePricingType.


        :param number_of_offer_listings: The number_of_offer_listings of this CompetitivePricingType.  # noqa: E501
        :type: NumberOfOfferListingsList
        """
        if number_of_offer_listings is None:
            raise ValueError("Invalid value for `number_of_offer_listings`, must not be `None`")  # noqa: E501

        self._number_of_offer_listings = number_of_offer_listings

    @property
    def trade_in_value(self):
        """Gets the trade_in_value of this CompetitivePricingType.  # noqa: E501


        :return: The trade_in_value of this CompetitivePricingType.  # noqa: E501
        :rtype: MoneyType
        """
        return self._trade_in_value

    @trade_in_value.setter
    def trade_in_value(self, trade_in_value):
        """Sets the trade_in_value of this CompetitivePricingType.


        :param trade_in_value: The trade_in_value of this CompetitivePricingType.  # noqa: E501
        :type: MoneyType
        """

        self._trade_in_value = trade_in_value

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
        if issubclass(CompetitivePricingType, dict):
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
        if not isinstance(other, CompetitivePricingType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
