$(() => {
    var pagePathName = window.location.pathname;
    var top_url = pagePathName.split("/")[1];

    if (top_url) {
      $("#" + top_url).addClass('active');
    }
});
