import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable, throwError } from 'rxjs';
import { catchError, retry } from 'rxjs/operators';

@Injectable({
  providedIn: 'root'
})
export class ThemoviedbService {

  private API_KEY;

  constructor(private http: HttpClient) {
    this.API_KEY = '0ca9f132991f891536e849fad2c94629';
   }

  getMovies(search: string) {
    return this.http.get<any>(`https://api.themoviedb.org/3/search/movie?api_key=${this.API_KEY}&language=en-US&query=${search}&page=1&include_adult=false`)
  }



}
