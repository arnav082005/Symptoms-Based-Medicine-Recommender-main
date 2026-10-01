async function getRecommendation() {

    const symptoms =
        document.getElementById("symptoms").value.trim();

    const loading =
        document.getElementById("loading");

    const result =
        document.getElementById("result");


    if (!symptoms) {

        alert("Please enter your symptoms.");

        return;
    }


    loading.style.display = "block";

    result.style.display = "none";


    try {

        const response = await fetch("/predict", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                symptoms: symptoms
            })

        });


        const data = await response.json();


        if (!response.ok) {

            alert(data.error || "Something went wrong.");

            return;
        }


        document.getElementById("medicine")
            .textContent = data.medicine;


        document.getElementById("confidence")
            .textContent = data.confidence;


        result.style.display = "block";

    }

    catch (error) {

        alert("Unable to connect to the server.");

    }

    finally {

        loading.style.display = "none";

    }
}