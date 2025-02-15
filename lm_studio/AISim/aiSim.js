dialog = [
    {
        "AI": "Hi, I need to know your phone number.",
        "victim": "Do you really?"
    },

    {
        "AI": "I need to give you information about your car's extended warranty",
        "victim": "I don't have a car."
    },

    {
        "AI": "Sorry, not your car, I mean your phone's extended warranty.",
        "victim": "In that case here you go: 212-555-6666"
    },

    {
        "AI": "Awesome. Thanks,",
        "victim": "Bye"
    },
]

dialog_i = 0;
aiDiv = null;
victimTxtBox = null;

function run_sim(ai_div_id, victim_TextBox_id){
    
    aiDiv = document.getElementById(ai_div_id);
    victimTxtBox = document.getElementById(victim_TextBox_id);
    // for (let i = 0; i < dialog.length; i++){

    //     console.log("i:", i)
    //     console.log("AI:", dialog[i]["AI"]);
    //     console.log("victim:", dialog[i]["victim"]);
    // }

    setTimeout(write_AI, 1000);
}


function write_AI(){
    let txt = dialog[dialog_i]["AI"];
    aiDiv.innerHTML = txt;
    setTimeout(write_victim, 1000);
}

function write_victim(){
    let txt = dialog[dialog_i]["victim"];
    victimTxtBox.value = txt;

    //increment for next interaction
    dialog_i += 1
    if (dialog_i < dialog.length){
        setTimeout(write_AI, 1000);
    }
}
