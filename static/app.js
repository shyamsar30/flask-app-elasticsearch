(function () {

    const quotesEl = document.querySelector('.quotes');
    const loaderEl = document.querySelector('.loader');

    // get the quotes from API
    const getQuotes = async (page, limit) => {
        console.log(window.location.href.split("q=")[1])
        const API_URL = `http://127.0.0.1:5000/get-response?q=${window.location.href.split("q=")[1]}&from=${page}`;

        const response = await fetch(API_URL);
        // handle 404
        if (!response.ok) {
            throw new Error(`An error occurred: ${response.status}`);
        }
        return await response.json();
    }

    // show the quotes
    const showQuotes = (quotes) => {
        quotes.forEach(quote => {
            const quoteEl = document.createElement('div');
            quoteEl.classList.add('quote');
            quoteEl.style.display = "inline-block";

            quoteEl.innerHTML = `
                    <style>
                        .sample{
                            background-image=url('https://images.unsplash.com/photo-1503023345310-bd7c1de61c7d?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8Mnx8aHVtYW58ZW58MHx8MHx8&w=1000&q=80')
                        }
                    </style>
                    <div class="card ml-5 mr-4 my-5" style="width:300px; height:570px">
                        <div class='sample', style="background-image:url(https://wallpapers.com/images/featured/xbsfzsltjksfompa.jpg');background-size: 200px;width:280px; height:350px;">
                      <img src=${quote.image}
                            class="card-img-top" style="width:106%; height:350px;"/>
                            </div>
                        <div class="card-body" style="width:200px; display: inline-block">
                            <div style='height: 50px'>
                            <h6 class="card-title">${quote.title.slice(0,35).concat("...")}</h6>
                            </div>
                            <p class="card-text">
                                ${quote.description.slice(0,35).concat("...")}
                            </p>
                            <p class="card-text" style:'margin-top:2px;'>
                                ${quote.store_name.slice(0,15).concat("...")}
                            </p>
                            <a href=${quote.page_link} target='_blank' class="btn btn-primary" style:'margin-down:2px;'>Product page</a>
                        </div>
                    </div>
        `;

            quotesEl.appendChild(quoteEl);
        });
    };

    const hideLoader = () => {
        loaderEl.classList.remove('show');
    };

    const showLoader = () => {
        loaderEl.classList.add('show');
    };

    const hasMoreQuotes = (page, limit, total) => {
        const startIndex = (page - 1) * limit + 1;
        return total === 0 || startIndex < total;
    };

    // load quotes
    const loadQuotes = async (page, limit) => {

        // show the loader
        showLoader();

        // 0.5 second later
        setTimeout(async () => {
            try {
                // if having more quotes to fetch
                console.log(page, limit, total)
                if (hasMoreQuotes(page, limit, total)) {
                    // call the API to get quotes
                    const response = await getQuotes(page, limit);
                    console.log(response)
                    // show quotes
                    showQuotes(response.data);
                    // update the total
                    total = response.total_records;
                    console.log(total)
                }
            } catch (error) {
                console.log(error.message);
            } finally {
                hideLoader();
            }
        }, 500);

    };

    // control variables
    let currentPage = 0;
    const limit = 20;
    let total = 0;


    window.addEventListener('scroll', () => {
        const {
            scrollTop,
            scrollHeight,
            clientHeight
        } = document.documentElement;

        if (scrollTop + clientHeight >= scrollHeight - 5 &&
hasMoreQuotes(currentPage, limit, total)) {
            currentPage++;
            loadQuotes(currentPage, limit);
        }
    }, {
        passive: true
    });

    // initialize
    loadQuotes(currentPage, limit);

})();