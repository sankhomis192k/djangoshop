var cartRow = document.querySelector("#cartRow");
if(cartRow !== null) cartRow.addEventListener("click",addToCart);


function addToCart(e){
	e.preventDefault();
	//let parentId = e.target.parentElement.parentElement.parentElement.getAttribute("id");
	let siblings = getSiblings(e.target);
	const productName = siblings[0].innerText;
	const productPrice = siblings[3].innerText
	let productImage = e.target.parentElement.parentElement.firstElementChild.getAttribute("src");
	let action = e.target.getAttribute("data-action");
	let productId = e.target.getAttribute("data-product");
	
	//if(user === 'AnonymousUser') 	
			
	manageCookieItem(productId,action);	
}

function manageCookieItem(productId,action){
	if(action === "add") {
		if(cookieCart[productId]) === undefined){
		cookieCart[productId] = { quantity: 1 }
		}
		else {
			cookieCart[productId]['quantity'] += 1 ;
		}
	}

	if(action === 'remove'){
		cookieCart[productId]['quantity'] -= 1;

		if(cookieCart[productId]['quantity'] <= 0){
			delete cookieCart[productId];
		}
	}

	document.cookie = "cookieCart="+JSON.stringify(cookieCart)+";domain=;path=/";
	
}


let getSiblings = function (e) {
    // for collecting siblings
    let siblings = []; 
    // if no parent, return no sibling
    if(!e.parentNode) {
        return siblings;
    }
    // first child of the parent node
    let sibling  = e.parentNode.firstChild;
    // collecting siblings
    while (sibling) {
        if (sibling.nodeType === 1 && sibling !== e) {
            siblings.push(sibling);
        }
        sibling = sibling.nextSibling;
    }
    return siblings;
};

function manageCart(e,productId,action){
		e.prventDefault();
		if(action === 'add'){
			cookieCart[productId] = {'quantity': 1};
		}
		else if(action === 'increase'){
			cookieCart[productId]['quantity'] += 1;
		}
		else if(action === 'decrease'){
			cookieCart[productId]['quantity'] -= 1;
			if(cookieCart[productId]['quantity'] <= 0){
				removeItem(productId);
			}
		}
		else {
			console.log('Invalid action');
		}

		document.cookie = "cookieCart="+JSON.stringify(cookieCart)+";domain=;path=/";
		window.location.reload();
}

function removeItem(productId){	
	delete cookieCart[productId];
	document.cookie = "cookieCart="+JSON.stringify(cookieCart)+";domain=;path=/";
}