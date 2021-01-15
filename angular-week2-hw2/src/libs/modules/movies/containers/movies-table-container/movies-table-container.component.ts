import { Component, OnDestroy, OnInit } from '@angular/core';
import { FormControl } from '@angular/forms';
import { combineLatest, of, Subscription } from 'rxjs';
import { debounceTime, startWith } from 'rxjs/operators';
import { IMovie } from '../../models/movie-models';
import { MoviesHttpService } from '../../services/movies-http.service';


@Component({
  selector: 'app-movies-table-container',
  templateUrl: './movies-table-container.component.html',
  styleUrls: ['./movies-table-container.component.scss']
})
export class MoviesTableContainerComponent implements OnInit, OnDestroy {

  movies: IMovie[];
  subscriptions: Subscription = new Subscription();
  _listFilter = '';
  get listFilter(): string {
    return this._listFilter;
  }
  set listFilter(value: string) {
    this._listFilter = value;
    this.filteredMovie = this.listFilter ? this.doFilter(this.listFilter) : this.movies;
  }

  filteredMovie: IMovie[] = [];
 
  constructor(private moviesHttpService: MoviesHttpService) {
    this.filteredMovie = this.movies;
    this.listFilter = '';
  }
  doFilter(filterBy: string): IMovie[] {
    filterBy = filterBy.toLocaleLowerCase();
    return this.movies.filter((movie: IMovie) =>
        movie.name.toLocaleLowerCase().indexOf(filterBy) !== -1);
  }
 


 
 

  ngOnInit(): void {
     
    
  
    
    this.subscriptions.add(
      this.moviesHttpService.getTop100Movies().subscribe((comments:any) =>{
       
        console.log(comments);
        this.movies= comments.filter((comment)=>{
          return comment.index <= 100;
        })
        
        
         
  
        
  
      })
     
    
      // TODO: assign filtered value (according to Form Input) to this.movies
      // Change all the code below here. This is just an example. 
      // Data should be taken from MoviesHttpService 
         
      // #region Example Code
     
      /*of([
        {
          "index": 16,
          "name": "The Matrix",
          "year": "1999",
          "rating": "8.6",
          "poster": "https://m.media-amazon.com/images/M/MV5BNzQzOTk3OTAtNDQ0Zi00ZTVkLWI0MTEtMDllZjNkYzNjNTc4L2ltYWdlXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_UX45_CR0,0,45,67_AL_.jpg"
        },
        {
          "index": 29,
          "name": "Interstellar",
          "year": "2014",
          "rating": "8.5",
          "poster": "https://m.media-amazon.com/images/M/MV5BZjdkOTU3MDktN2IxOS00OGEyLWFmMjktY2FiMmZkNWIyODZiXkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_UY67_CR0,0,45,67_AL_.jpg"
        },
        {
          "index": 34,
          "name": "The Lion King",
          "year": "1994",
          "rating": "8.5",
          "poster": "https://m.media-amazon.com/images/M/MV5BYTYxNGMyZTYtMjE3MS00MzNjLWFjNmYtMDk3N2FmM2JiM2M1XkEyXkFqcGdeQXVyNjY5NDU4NzI@._V1_UY67_CR0,0,45,67_AL_.jpg"
        }
      ]).subscribe((movies) => {
        this.movies = movies;
      })*/
      // #endregion
    )


  }
  /*applyFilter(filterValue: string) {
    let filterValueLower = filterValue.toLowerCase();
    if(filterValue === '' ) {
        this.movies=this.movies;
    } 
    else {
      this.movies= this.movies.filter((movie) => movie.name.includes(filterValueLower))
    }
 }*/


  ngOnDestroy() {
    this.subscriptions.unsubscribe();
  }

}
