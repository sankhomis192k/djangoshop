const CART = {
	KEY:key,
	contents:[],
	init(){		
		let contents = localStorage.getItem(CART.KEY);
		if(contents){	
			console.log('cart exists');		
			CART.contents = contents;
		}		
	},
	async sync(){
		let cart = JSON.stringify(CART.contents);
		await localStorage.setItem(CART.KEY,cart);
	},
	find(id){
		let match = CART.contents.filter(item=>{
			return item.id = id
		});

		if( match && match[0]){
			return match[0];
		}
	},
	add(cartItem){
		CART.contents.push(cartItem);
		CART.sync();
	}
}
window.addEventListener("DOMContentLoaded",function(){	
	CART.init();
});

