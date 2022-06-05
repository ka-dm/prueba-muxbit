import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { PageComponent } from './components/page/page.component';
import { HeaderComponent } from './components/header/header.component';
import { BodyComponent } from './components/body/body.component';
import { SearchMovieComponent } from './components/search-movie/search-movie.component';
import { MovieCardComponent } from './components/search-movie/movie-card/movie-card.component';
import { PageSearchMovieComponent } from './components/search-movie/page-search-movie/page-search-movie.component';

@NgModule({
  declarations: [
    AppComponent,
    PageComponent,
    HeaderComponent,
    BodyComponent,
    SearchMovieComponent,
    MovieCardComponent,
    PageSearchMovieComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
