# Changelog for project chess21
### Unreleased:
##### Main goals:
- sign up/login form
- chess board
- rating/stats
- database
- matchmaking system
- all pages
##### Design:
- styles for all pages
- bootstrap?
- black theme (optional)

## [0.1.3] - 2023-04-04
### Added
- PostgreSQL database
- tables for games and moves
### Removed
- SQLite database

*****
## [0.1.2] - 2023-03-31
### Added
- moves validation
- stockfish engine
- moves analyzation (python print)
- enemy ai (black moves are replayed by stockfish)
- end game alert (only in no AI mode now)
*****
## [0.1.1] - 2023-03-29
### Added
- Chessboard
- New application for it
- Installed python-chess library
- Installed stockfish engine

### Removed
- "check in" application
*****
## [0.1.0] - 2023-03-27
### Added
- Basic django project
- 2 applications - "main pages" and "check in"
- Some urls and templates