getUrlVars();

function getUrlVars() {
    var vars = {};
    var parts = window.location.href.replace(/[?&]+([^=&]+)=([^&]*)/gi, function(m,key,value) {
        vars[key] = value;
    });
    return vars.type;
}

function displayTools(type) {
    //TODO: When the backend is hooked up loop through tools and display ones with this type
}
