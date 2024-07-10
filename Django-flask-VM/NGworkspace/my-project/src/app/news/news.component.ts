import { Component, OnInit, ViewChild } from '@angular/core';
import { NewsService} from '../news.service';

@Component({
  selector: 'app-news',
  templateUrl: './news.component.html',
  styleUrl: './news.component.css'
})
export class NewsComponent implements OnInit {
  newsdata: any[] = [];
  err: any;

  // @ViewChild(MatPaginator) paginator: MatPaginator;

  constructor(private newsService: NewsService) { }

  ngOnInit(): void {
    // this.newsdata.paginator = this.paginator

    this.newsService.getNews().then((data) => {
      this.newsdata = data['articles'];
      console.log(data);
    });
  }
}
