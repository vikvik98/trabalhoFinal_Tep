import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Filme } from '../filme';


@Component({
  selector: 'app-filmes',
  templateUrl: './filmes.component.html',
  styleUrls: ['./filmes.component.css']
})
export class FilmesComponent implements OnInit {
  private filmeUrl = 'http://localhost:8000/filmes/';
  private filmes = Array<Filme>();

  constructor(private http: HttpClient) { }

  ngOnInit() {
    this.http.get(this.filmeUrl).subscribe(response => this.getFilmes(response));
  }
  getFilmes(response): void {
    for (const filme of response) {
      this.filmes.push(new Filme(filme.id, filme.nome, filme.categoria));
    }
  }

}
