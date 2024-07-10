import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { FriendsComponent } from './friends/friends.component';
import { EmployessComponent } from './employess/employess.component';

const routes: Routes = [
  {path: 'friends', component: FriendsComponent },
  {path: 'employess', component: EmployessComponent}
];


@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
