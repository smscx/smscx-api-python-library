# DataOptouts


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Identifier of the optout | 
**phone_number** | **str** | Phone number in international E.164 format | 
**country_iso** | **str** | Two-letter country ISO of the phone number that unsubscribed | 
**optout_from** | **str** | Type of optout. **admin** if the contact has been manually added by the admin or **link** if the contact has clicked the optout link | 
**datetime** | **str** |  | 
**campaign_id** | **str, none_type** | Identifier of the campaign from which the contact has unsubscribed | [optional] 
**group_id** | **str, none_type** | Identifier of the group the contact was in | [optional] 
**group_name** | **str** | Name of the group the contact was in | [optional] 
**campaign_name** | **str, none_type** | Name of the campaign from which the contact has unsubscribed | [optional] 


[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#available-methods) [[Back to README]](../../README.md)


