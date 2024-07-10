import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { LaptopComponent } from './laptop/laptop.component';

const routes: Routes = [
  {path:"laptop", component:LaptopComponent},
  // { path: 'lap/:Id', component: EmpDetailComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
