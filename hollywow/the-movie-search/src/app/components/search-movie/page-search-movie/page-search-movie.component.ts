import { Component, OnInit } from '@angular/core';
import { ThemoviedbService } from '../../../services/themoviedb.service';


@Component({
  selector: 'app-page-search-movie',
  templateUrl: './page-search-movie.component.html',
  styleUrls: ['./page-search-movie.component.scss']
})
export class PageSearchMovieComponent implements OnInit {

  movieName: string;

  constructor(private themoviedbService: ThemoviedbService) {
    this.movieName = "";
  }

  ngOnInit(): void {
  }

  onSubmit() {
    alert("Su pelicula se llama " + this.movieName); 
    this.themoviedbService.getMovies(this.movieName);
  }
  
  
}
