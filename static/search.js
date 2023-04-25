const input = document.querySelector('.search');
const suggestions = document.querySelector('.suggestions ul');
async function getresult(inputVal){
        const API_URL = `http://${window.location.host}/autocomplete?s=${inputVal[0].value}`;
        console.log(API_URL)
        const response = await fetch(API_URL);
        // handle 404
        if (!response.ok) {
            throw new Error(`An error occurred: ${response.status}`);
        }
//        console.log(response.json())
        return await response.json();
    }

async function searchHandler(e) {
	const inputVal = document.getElementsByClassName('search');
	console.log(inputVal)
	let results = [];
	if (inputVal.length > 0) {
		const response = await getresult(inputVal);
		results=response.data

	}
	showSuggestions(results, inputVal);
}

function showSuggestions(results, inputVal) {
    console.log(results)
    suggestions.innerHTML = '';

	if (results.length > 0) {
	    document.getElementById("search_div").classList.remove("d-none");
//	    document.getElementById("no-data").classList.add("transp");
		for (i = 0; i < results.length; i++) {
			let item = results[i];
			// Highlights only the first match
			// highlight all matches
            try{
                const match = item.match(new RegExp(inputVal[0].value, 'i'));
                item = item.replace(match[0], `<strong>${match[0]}</strong>`);
			    }
			catch(err){

			}
			suggestions.innerHTML += `<ul>${item}</ul>`;
		}
		suggestions.classList.add('has-suggestions');
	} else {
		document.getElementById("search_div").classList.add("d-none");
		results = [];
		suggestions.innerHTML = '';
		suggestions.classList.remove('has-suggestions');
	}
}

function useSuggestion(e) {
	document.getElementById("search_div").classList.add("d-none");
	input.value = e.target.innerText;
	input.focus();
	suggestions.innerHTML = '';
	suggestions.classList.remove('has-suggestions');
}

input.addEventListener('keyup', searchHandler);
suggestions.addEventListener('click', useSuggestion);
