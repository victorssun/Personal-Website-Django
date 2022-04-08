function get_request() {
    var search_field = document.getElementById('search').value;
    var data = document.querySelector('input[name="radios"]:checked').value;
    var page_num = document.getElementById('page_num').value;

    $.ajax({
        url: "/pf/api/" + data + "?search=" + search_field + "&page=" + page_num,
        type: 'GET',
        dataType: 'json',
        success: function(resp) {
            var table_headers = "<tr>";
            var table_data = "";
            resp = resp["results"];

            if (resp.length == 0) {
                return document.getElementById("output").innerHTML = "No data.";
            }

            // get table headers from first row
            for (const key in resp[0]) {
                table_headers = table_headers + "<th>" + key + "</th>";
            }
            table_headers = table_headers + "</tr>";

            // get table data
            for(var i=0; i<resp.length; i++){
                table_data = table_data + "<tr>";
                for(const key in resp[i]){
                    table_data = table_data + "<td>" + resp[i][key] + "</td>";

                }
                table_data = table_data + "</tr>";
            }

            document.getElementById("output").innerHTML = table_headers + table_data;
        },
        error: function(xhr, status, error) {
            document.getElementById("output").innerHTML = xhr.status + ": " + xhr.responseText;
        }
    });
}
