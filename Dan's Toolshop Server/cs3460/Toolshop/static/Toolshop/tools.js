toolsList = toolsList.filter((first, second) => toolsList.indexOf(first) === second)

// THESE MODIFY THE DOM, DISPLAYING THE INFO THE USER HAS ASKED FOR
function displayBike() {
    var bikeTools = toolsList.slice(0, 3);
    existingDiv = document.getElementById("tool_info_section");
    existingDiv.removeChild(existingDiv.firstChild);
    newDiv = document.createElement('div');


    p = document.createElement('p');
    p.textContent = "In need of top-quality tools for your next ride?  With our bike tools, you will always have the " +
    "equipment you need to ride safely and with confidence.  Check out our current stock below:";
    newDiv.appendChild(p);

    bikeTools.forEach(tool =>{
        p = document.createElement('p');
        p.textContent = tool;
        newDiv.appendChild(p);
    })

    existingDiv.appendChild(newDiv);
}
function displayCarpentry() {
    var carpentryTools = toolsList.slice(3, 35);
    existingDiv = document.getElementById("tool_info_section");
    existingDiv.removeChild(existingDiv.firstChild);
    newDiv = document.createElement('div');


    p = document.createElement('p');
    p.textContent = "Interested in woodworking? Whether you're a pro or a beginner these tools will help you create masterpieces. " +
    "Check out our current stock below:";
    newDiv.appendChild(p);

    carpentryTools.forEach(tool =>{
        p = document.createElement('p');
        p.textContent = tool;
        newDiv.appendChild(p);
    })

    existingDiv.appendChild(newDiv);
}
function displayCarpet() {
    var carpetTools = toolsList.slice(35, 40);
    existingDiv = document.getElementById("tool_info_section");
    existingDiv.removeChild(existingDiv.firstChild);
    newDiv = document.createElement('div');


    p = document.createElement('p');
    p.textContent = "Is it time for new flooring?  How about some nice carpet? " +
    "We have all of the tools to help you do it yourself.  Check out our current stock below:";
    newDiv.appendChild(p);

    carpetTools.forEach(tool =>{
        p = document.createElement('p');
        p.textContent = tool;
        newDiv.appendChild(p);
    })

    existingDiv.appendChild(newDiv);
}
function displayCement() {
    var cementTools = toolsList.slice(40, 45);
    existingDiv = document.getElementById("tool_info_section");
    existingDiv.removeChild(existingDiv.firstChild);
    newDiv = document.createElement('div');


    p = document.createElement('p');
    p.textContent = "With our collection of tools, there's no need to hire someone to fix your driveway or patio! " +
    "Check out our current stock below:";
    newDiv.appendChild(p);

    cementTools.forEach(tool =>{
        p = document.createElement('p');
        p.textContent = tool;
        newDiv.appendChild(p);
    })

    existingDiv.appendChild(newDiv);
}
function displayDrywall() {
    var drywallTools = toolsList.slice(45, 56);
    existingDiv = document.getElementById("tool_info_section");
    existingDiv.removeChild(existingDiv.firstChild);
    newDiv = document.createElement('div');


    p = document.createElement('p');
    p.textContent = "Did your child or pet knock a hole into the wall again? With our tools, fixing it will be a breeze!" +
    "Check out our current stock below:";
    newDiv.appendChild(p);

    drywallTools.forEach(tool =>{
        p = document.createElement('p');
        p.textContent = tool;
        newDiv.appendChild(p);
    })

    existingDiv.appendChild(newDiv);
}
function displayElectrical() {
    var electricalTools = toolsList.slice(56, 77);
    existingDiv = document.getElementById("tool_info_section");
    existingDiv.removeChild(existingDiv.firstChild);
    newDiv = document.createElement('div');


    p = document.createElement('p');
    p.textContent = "With our tools and a can-do attitude, you can solve any problem! Use our electical and mechanical tools " +
    "for your next project! Check out our current stock below:";
    newDiv.appendChild(p);

    electricalTools.forEach(tool =>{
        p = document.createElement('p');
        p.textContent = tool;
        newDiv.appendChild(p);
    })

    existingDiv.appendChild(newDiv);
}
function displayGarden() {
    var gardenTools = toolsList.slice(77, 110);
    existingDiv = document.getElementById("tool_info_section");
    existingDiv.removeChild(existingDiv.firstChild);
    newDiv = document.createElement('div');


    p = document.createElement('p');
    p.textContent = "There's nothing like getting your hands dirty in the garden. That's why we offer a wide variety of gardening equipment " +
    "so your yard can look amazing and make you the talk of the neighborhood!  Check out our current stock below:";
    newDiv.appendChild(p);

    gardenTools.forEach(tool =>{
        p = document.createElement('p');
        p.textContent = tool;
        newDiv.appendChild(p);
    })

    existingDiv.appendChild(newDiv);
}
function displayPower() {
    var powerTools = toolsList.slice(132, 166);
    existingDiv = document.getElementById("tool_info_section");
    existingDiv.removeChild(existingDiv.firstChild);
    newDiv = document.createElement('div');


    p = document.createElement('p');
    p.textContent = "Can you handle the power? These power tools will be sure to speed up your project so you can quickly " +
    "move on to the next one!  Check out our current stock below:";
    newDiv.appendChild(p);

    powerTools.forEach(tool =>{
        p = document.createElement('p');
        p.textContent = tool;
        newDiv.appendChild(p);
    })

    existingDiv.appendChild(newDiv);
}
function displayKitchen() {
    var bikeTools = toolsList.slice(110, 114);
    existingDiv = document.getElementById("tool_info_section");
    existingDiv.removeChild(existingDiv.firstChild);
    newDiv = document.createElement('div');


    p = document.createElement('p');
    p.textContent = "Are you a genious in the kitchen? Even if you're not, create some delicious items with our collection " +
    "of kitchen equipment. Check out our current stock below:";
    newDiv.appendChild(p);

    bikeTools.forEach(tool =>{
        p = document.createElement('p');
        p.textContent = tool;
        newDiv.appendChild(p);
    })

    existingDiv.appendChild(newDiv);
}
function displayOther() {
    var bikeTools = toolsList.slice(114, 132);
    existingDiv = document.getElementById("tool_info_section");
    existingDiv.removeChild(existingDiv.firstChild);
    newDiv = document.createElement('div');


    p = document.createElement('p');
    p.textContent = "Can't find what you want? Check out our other items, you never know what you'll find. " +
    " Check out our current stock below:";
    newDiv.appendChild(p);

    bikeTools.forEach(tool =>{
        p = document.createElement('p');
        p.textContent = tool;
        newDiv.appendChild(p);
    })

    existingDiv.appendChild(newDiv);
}