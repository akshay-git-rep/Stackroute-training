import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { Django1Component } from './django1/django1.component';
import { NewsComponent } from './news/news.component';
import { EmpsComponent } from './emps/emps.component';
import { StudentsComponent } from './students/students.component';
import { ProfileComponent } from './profile/profile.component';

const routes: Routes = [
  {path:"django1", component:Django1Component},
  {path:"news", component:NewsComponent},
  {path:"emps", component:EmpsComponent},
  {path:"students", component:StudentsComponent},
  {path:"profile", component:ProfileComponent},
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
