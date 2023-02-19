# DataShortlinkHit

Event type data, grouped in multiple objects (up to 200 in a request)

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hit_id** | **int** |  | 
**shortlink_id** | **str** | ID of the short link | 
**url** | **str** | URL of the short link | 
**device** | **str** | Type of device of the visitor | 
**browser** | **str** | Type of browser of the visitor that accessed the short link | 
**browser_version** | **str** | Browser version of the device that accessed the short link | 
**os** | **str** | Operating system of the visitor that accessed the short link (eg. Android, Windows, Linux, etc.) | 
**os_version** | **str** | Version of the operating system | 
**brand** | **str** | Brand of phone/tablet of the visitor that accessed the short link | 
**model** | **str** | Model of phone/tabled of the visitor that accessed the short link (eg. P30 Pro, Galaxy S8, etc.) | 
**screen_resolution** | **str** |  | 
**accept_language** | **str** |  | 
**referrer** | **str, none_type** |  | 
**ip_address** | **str** | Anonymized IP address without the last byte. Eg. &#x60;204.79.200.0&#x60; | 
**country_iso** | **str** | Two-letter country ISO of the visitor that accessed the short link | 
**city** | **str** | The city of the visitor that accessed the short link | 
**datetime** | **str** |  | 
**phone_number** | **str** | Phone number of the visitor that made the hit to the shortlink (works if link tracking option is used when sending a message). If short link tracking was enabled, this parameter will not be null.  | [optional] 
**campaign_id** | **str, none_type** | Identifier of the campaign from which the contact has made the visit. If short link tracking was enabled, this parameter will not be null. | [optional] 
**group_id** | **str, none_type** | Identifier of the group the contact is in. If short link tracking was enabled, this parameter will not be null. | [optional] 


[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#available-methods) [[Back to README]](../../README.md)


