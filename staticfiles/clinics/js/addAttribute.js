function addAttribute()
{
    var h2_list = document.getElementsByClassName("description_markdown")[0].getElementsByTagName("h2");
    const tag_name = ["gioithieu", "themanh", "thietbi", "vitri"];
    h2_list[0].setAttribute('id', tag_name[0]);
    h2_list[1].setAttribute('id', tag_name[1]);
    h2_list[2].setAttribute('id', tag_name[2]);
    h2_list[3].setAttribute('id', tag_name[3]);
}
  
addAttribute();