#include<iostream>
#include <algorithm>
#include<vector>
#include<string>


enum CellStatus
{
    Hidden = 0,
    Flagged = 1,
    Unhidden = 2,
    Explode = 3
};

class Cell
{

private:
    int content = 0;
    bool isbomb = false;
    CellStatus status = CellStatus::Hidden;

   protected:
    virtual void setIsBomb(bool isbomb){ this->isbomb = isbomb; }
    virtual void setStatus(CellStatus newstatus){ this->status = newstatus; }

    public:

    /// @brief Konstruktor domyślny
    Cell()
    {
        status = CellStatus::Hidden;
        content = 0;
    }

    bool getIsBomb(){ return this->isbomb; }
    int getContent(){ return this->content; }
    void setContent(int content) { this->content = content; }
    CellStatus getStatus(){ return this->status;  }

    /// @brief Puts flag on cell
    /// Only when status is hidden
    virtual void flag()
    {
        if(getStatus() == CellStatus::Hidden)
        {
            setStatus(CellStatus::Flagged);
        }
    }

    virtual void unflag()
    {
        if(getStatus() == CellStatus::Flagged)
        {
            setStatus(CellStatus::Hidden);
        }
    }


    /// \brief Puts bomb to cell
    /// Only when status is hidden
    void putBomb()
    {
        if(getStatus() == CellStatus::Hidden)
            setIsBomb(true);
    }

    /// @brief Sets Cell to visible with no test.
    /// Should be used after game finish and on
    /// cells that did not explode
    virtual void show()
    {
        if(getStatus()!= CellStatus::Explode)
        {
            setStatus(CellStatus::Unhidden);
        }
    }

    /// @brief Minesweeper check cell function
    /// @return Returns true if test cell is not bomb and false is cell is bomb
    virtual void check()
    {
        if(getStatus()!=CellStatus::Hidden) return;
        if(getIsBomb())
        {
            setStatus(CellStatus::Explode);
        }
        else
        {
            setStatus(CellStatus::Unhidden);
        }
    }
};

enum GameStatus{NotStarted, Started, Won, Lost};

enum GameLevel{Easy, Medium , Hard};

class Game
{
    int rows=9, cols=9, bombs=10;
    Cell * board = nullptr; // tablica komórek
    GameStatus status=GameStatus::NotStarted;
    GameLevel level=GameLevel::Easy;
    protected:
    void setStatus(GameStatus status) { this->status = status;}
    void setRows(int rows) {this->rows = rows;}
    void setCols(int cols) {this->cols = cols;}
    void setBombs(int bombs) {this->bombs = bombs;}
    int getBombs() { return bombs; }

    void createBoard()
    {
        //sprawdzenie czy w obiekcie jest
        //już zadeklarowana plansza
        if(board != nullptr)
        {
            //kasowanie planszy
            delete[] board;
        }
        int N = rows * cols;
        // przydzielenie pamięci dla planszy
        board = new Cell[N];
    }

    void putBombs()
    {
        int N = rows*cols;
        int * ids = new int[N];
        // wypełnianie buffora ids liczbami od 0 do N-1
        for (int i = 0; i< N; i++)
        {
            ids[i] = i;
        }
        // losowa zmiana kolejnosci elementów buffora ids
        std::srand(time(0));
        std::random_shuffle(ids,ids+N);
        for (int b = 0; b<bombs; b++)
        {
            board[ids[b]].putBomb();
            //zwiększenie content o 1 w otoczeniu gry
            int x = ids[b]/cols;
            int y = ids[b]%cols;
            for(int i=x-1; i<=x+1; i++)
            {
                for(int j=y-1;j<=y+1;j++)
                {
                    if(j!=i && checkIds(this,i,j))
                    {
                        int cnt = board[from2D(this,i,j)].getContent();
                        board[from2D(this,i,j)].setContent(cnt+1);
                    }
                }
            }
        }
    }

    void showAll()
    {
        int N = this->getRows()*this->getCols();
        for(int n =0; n<N; n++)
        {
            board[n].show();
        }
    }

    public:
    Game()
    {
        //test tworzenia planszy
        rows=10;
        cols=10;
        createBoard();
    }

    GameStatus getStatus() {return status;}
    GameLevel getLevel() {return level;}
    void setLevel(GameLevel level)
    {
        if(getStatus()==GameStatus::NotStarted)
        {
            this->level =level;
            switch(this->level)
            {
                case GameLevel::Easy:
                setRows(9);
                setCols(9);
                setBombs(10);
                break;
                case GameLevel::Medium:
                setRows(16);
                setCols(16);
                setBombs(40);
                break;
                case GameLevel::Hard:
                setRows(16);
                setCols(30);
                setBombs(99);
                break;
            }
            createBoard();
        }
    }

    int getRows() { return rows;}
    int getCols() { return cols;}

    // przeliczanie indeksów 2D na 1D
    static int from2D(Game* game,int x, int y)
    {
        return x * game->getCols() + y;
    }

    static bool checkIds(Game* game, int x, int y)
    {
        if(x<0 || x>=game->getRows()) return false;
        if(y<0 || y>=game->getCols()) return false;
        return true;
    }

    void start()
    {
        if(getStatus()==GameStatus::NotStarted)
        {
            setStatus(GameStatus::Started);
            putBombs();
        }
    }

    void reset()
    {
        if(getStatus()!=GameStatus::NotStarted)
        {
            setStatus(GameStatus::NotStarted);
            createBoard();
        }
    }

    void win()
    {
        if(getStatus()==GameStatus::Started)
        {
            setStatus(GameStatus::Won);
            showAll();
        }
    }

    void lose()
    {
        if(getStatus()==GameStatus::Started)
        {
            setStatus(GameStatus::Lost);
            showAll();
        }
    }

    Cell* operator[](int index)
    {
        return board + index;
    }
};
