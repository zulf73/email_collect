(function($){'use strict';jQuery(document).ready(function(){var disc_modules=jQuery('.nus-discovery-module');disc_modules.each(function(){var this_module=jQuery(this);var this_content=this_module.find('.nus-discovery-content');var input_search=this_module.find('#nus-discovery-search');var input_cat=this_module.find('#nus-discovery-cat');var input_group=this_module.find('#nus-discovery-group');var submit_search=this_module.find('#nus-discovery-button');var reset_button=this_module.find('#nus-discovery-reset');load_discovery_content(this_module,this_content,input_search,input_cat,input_group,submit_search,false);reset_button.on('click',function(){this_content.empty();input_cat.empty();input_group.empty();load_discovery_content(this_module,this_content,input_search,input_cat,input_group,submit_search,true);});});});})(jQuery);function load_discovery_content(this_module,this_content,input_search,input_cat,input_group,submit_search,is_reset){var dept_id=this_content.data('dept_id');var profile_id=this_content.data('profile_id');jQuery.ajax({"url":nus_discovery.ajax_url,"data":{"action":"get_xml","dept_id":dept_id,"profile_id":profile_id,"is_reset":is_reset,"get_nonce":nus_discovery.nus_get_xml_nonce},"dataType":"html","method":"POST","beforeSend":function(){submit_search.off('click');},"success":function(html){this_content.append(html);var departments=this_module.find('#nus-discovery-departments .dept-list');var groups=this_module.find('#nus-discovery-primarygroup .group-list');departments.each(function(){var the_value=jQuery(this).text();input_cat.append('<option value="'+the_value+'">'+the_value+'</option>');});groups.each(function(){var the_value=jQuery(this).text();input_group.append('<option value="'+the_value+'">'+the_value+'</option>');});submit_search.on('click',function(){var search=input_search.val().toUpperCase();var dept_search=input_cat.val().toUpperCase();var lists=jQuery('.nus-discovery-table-content > li');lists.each(function(){var the_list=jQuery(this);var name=the_list.data('name');var dept=the_list.data('department');var primarygrp=the_list.data('primarygroup');var dept_display=false;var name_display=false;if(dept.toUpperCase().indexOf(dept_search)>-1){dept_display=true;}
if(name.toUpperCase().indexOf(search)>-1){name_display=true;}
if(dept_display&&name_display){the_list.css('display',"");}else{the_list.css('display',"none");}});});}});}