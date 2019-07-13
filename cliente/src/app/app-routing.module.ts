import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { LoginComponent } from './login/login.component';
import { FilmesComponent } from './filmes/filmes.component';
import { CategoriasComponent } from './categorias/categorias.component';

const routes: Routes = [
  { path: 'login', component: LoginComponent },
  { path: 'filmes', component: FilmesComponent },
  { path: 'categorias', component: CategoriasComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
