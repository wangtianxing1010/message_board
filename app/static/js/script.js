$(function(){
    function render_time(){
        return moment($(this).data("timestamp")).format("LLL")
    }
    $('[data-toggle="tooltip"]').tooltip(
        {title:render_time}
    );

});