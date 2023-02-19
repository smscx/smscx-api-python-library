# DataNewOptout

Event data, grouped in multiple objects (up to 200 in a request)

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hit_id** | **int** |  | 
**optout_id** | **str** | ID of the optout link | 
**optout_url** | **str** | URL of the optout link | 
**optout_type** | **str** | The method by which the contact has unsubscribed. Value &#x60;link&#x60; means he clicked on the optout link and submitted the form and value &#x60;admin&#x60; it means that the client was added to the optout list by you | 
**country_iso** | **str** | Two-letter country ISO of the phone number that unsubscribed. | 
**datetime** | **str** |  | 
**phone_number** | **str** | Phone number that choose to opt out.  | [optional] 
**campaign_id** | **str, none_type** | Identifier of the campaign from which the contact has unsubscribed. If optout tracking was enabled, this parameter will not be null. | [optional] 
**group_id** | **str, none_type** | Identifier of the group the contact was in. If optout tracking was enabled, this parameter will not be null. | [optional] 


[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#available-methods) [[Back to README]](../../README.md)


