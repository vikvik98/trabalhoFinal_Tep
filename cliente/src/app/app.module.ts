import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { HttpClientModule, HttpClient, HTTP_INTERCEPTORS } from '@angular/common/http';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { LoginComponent } from './login/login.component';
import { AuthService, AuthGuard, AuthInterceptor } from './auth.service';
import { FilmesComponent } from './filmes/filmes.component';
import { CategoriasComponent } from './categorias/categorias.component';


@NgModule({
  declarations: [
    AppComponent,
    LoginComponent,
    FilmesComponent,
    CategoriasComponent
  ],
  imports: [
    HttpClientModule,
    BrowserModule,
    AppRoutingModule
  ],
  providers: [
    HttpClient,
    AuthService,
    AuthGuard,
    {
      provide: HTTP_INTERCEPTORS,
      useClass: AuthInterceptor,
      multi: true,
    },
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
