

query_one = """"
              SELECT articles.title,count(log.path) from log  join articles on log.path =
            concat('/article/',articles.slug)  GROUP BY articles.title order by count
            desc limit 3;
            """


query_two = """"
          select authors.name ,authorcount.count from authors join
          (SELECT articles.author ,count(log.path) from log join articles on log.path =
          concat('/article/',articles.slug) GROUP BY articles.author) as authorcount on
          authors.id = authorcount.author order by authorcount.count desc;
          """



query_three = """"
         select * from
         (select main.alldays , round(cast((100*main.faultcount) AS NUMERIC ) / cast(main.totalcount AS NUMERIC ), 2) as e from
         ((select date(time) as alldays ,count(*) as totalcount from log group by alldays) as x join
         (select date(time) as faultdays ,count(*)as faultcount from log  where status LIKE '%404%' group by faultdays) as fault on
         x.alldays = fault.faultdays) as main) as  y where y.e>1.0;
         """
