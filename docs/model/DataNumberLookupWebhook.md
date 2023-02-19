# DataNumberLookupWebhook


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**phone_number** | **str** | Phone number in international E.164 format | 
**lookup_bulk_id** | **str, none_type** | Unique bulk lookup identifier | 
**lookup_id** | **str** | Unique lookup identifier | 
**cost** | **float** | The cost of phone number lookup | 
**mcc** | **str** | Mobile country code. [See full list of MCC](https://www.itu.int/dms_pub/itu-t/opb/sp/T-SP-E.212B-2018-PDF-E.pdf) | 
**mccmnc** | **str** | Mobile country code + Mobile network code. [See full list of MCC + MNC](https://www.itu.int/dms_pub/itu-t/opb/sp/T-SP-E.212B-2018-PDF-E.pdf) | 
**country_iso** | **str** | Two-letter country code in ISO-3166 alpha 2 standard of the destinations. Eg. &#x60;DE&#x60;, &#x60;FR&#x60;, &#x60;IT&#x60; | 
**country_name** | **str** | Name of the country of the phone number | 
**country_name_locale** | **str** | Name of the country in local language | 
**status** | **str** | Status of the phone number | 
**status_description** | **str** | Short description of the status | 
**ported** | **bool** | Returns &#x60;true&#x60; if the phone number is ported to other mobile network, &#x60;false&#x60; otherwise | 
**roaming** | **bool** | Returns &#x60;true&#x60; if the phone number is roaming in other network, &#x60;false&#x60; otherwise | 
**original_network** | [**OriginalNetwork**](OriginalNetwork.md) |  | 
**ported_network** | [**PortedNetwork**](PortedNetwork.md) |  | 
**roaming_network** | [**RoamingNetwork**](RoamingNetwork.md) |  | 
**datetime** | **datetime** | Date and time of the phone number lookup request | 


[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#available-methods) [[Back to README]](../../README.md)


