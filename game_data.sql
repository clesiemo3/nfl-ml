select
    g.gsis_id,
	g.week,
	g.season_type,
	g.start_time,
	d.pos_team,
	sum(ap.passing_yds) passing_yds,
	sum(ap.rushing_yds) rushing_yds,
	sum(ap.puntret_yds) puntret_yds,
	sum(ap.kickret_yds) kickret_yds,
case 	when d.pos_team = g.home_team then g.home_score
	when d.pos_team = g.away_team then g.away_score
	end score,
case 	when d.pos_team = g.home_team then true
	when d.pos_team = g.away_team then false
	end home
from drive d
join game g on g.gsis_id = d.gsis_id
join agg_play ap on ap.drive_id = d.drive_id and ap.gsis_id = d.gsis_id
where g.season_year = 2016
group by g.gsis_id, d.pos_team, g.week, g.season_type, g.start_time;