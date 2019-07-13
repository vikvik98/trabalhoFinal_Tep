import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Router } from '@angular/router';
import { Categoria } from '../categoria';


@Component({
  selector: 'app-categorias',
  templateUrl: './categorias.component.html',
  styleUrls: ['./categorias.component.css']
})
export class CategoriasComponent implements OnInit {
  private categoriaUrl = 'http://localhost:8000/categorias/';
  private categorias = Array<Categoria>();

  constructor(private http: HttpClient, private router: Router) { }

  ngOnInit() {
    this.http.get(this.categoriaUrl).subscribe(response => this.getCategorias(response));
  }

  getCategorias(response): void {
    console.log(response)
    for (const categoria of response) {
      this.categorias.push(new Categoria(categoria.id, categoria.nome));
    }
  }

  post(nome: string) {
    this.http.post(this.categoriaUrl,
      {nome: nome}).subscribe(
      response => window.location.reload(),
      error1 => console.log(error1)
    );
    
  }

}
