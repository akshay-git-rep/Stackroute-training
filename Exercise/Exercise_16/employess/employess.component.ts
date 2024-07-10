import { Component } from '@angular/core';

@Component({
  selector: 'app-employess',
  templateUrl: './employess.component.html',
  styleUrl: './employess.component.css'
})
export class EmployessComponent {
  id: string="";
  name:string="";
  salary= 0
  taxAmount=0

  getTax(){
    this.taxAmount = this.salary * 0.1 
  }
}


