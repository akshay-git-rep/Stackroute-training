import { Component } from '@angular/core';
import { Product } from './product.interface';

@Component({
  selector: 'app-product',
  templateUrl: './product.component.html',
  styleUrl: './product.component.css'
})
export class ProductComponent {
  products: Product[] = [
    { name: 'Laptop', price: 1200, category: 'Electronics' },
    { name: 'Shirt', price: 25, category: 'Clothing' },
    { name: 'Headphones', price: 75, category: 'Electronics' },
    { name: 'Dress', price: 50, category: 'Clothing' },
    { name: 'Coffee Maker', price: 80, category: 'Home' },
  ];
listed = [];
  selectedCategory: string = '';
  get filteredProducts(){
    if (this.selectedCategory == 'All Categories'){
      return this.products;
    }
    else (this.selectedCategory != 'All Categories') ;{
      return this.products.filter((item) => item.category == this.selectedCategory);
    }  
  }
 
}
