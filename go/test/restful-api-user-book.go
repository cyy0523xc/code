package main

import (
	"fmt"
	"github.com/ant0ine/go-json-rest/rest"
	"log"
	"net/http"
	"sync"
)

func main() {

	users := Users{
		Store: map[string]*User{},
	}

	books := Books{
		Store: map[string]*Book{},
	}

	api := rest.NewApi()
	api.Use(rest.DefaultDevStack...)
	router, err := rest.MakeRouter(
		// users router
		rest.Get("/users", users.GetAllUsers),
		rest.Post("/users", users.PostUser),
		rest.Get("/users/:id", users.GetUser),
		rest.Put("/users/:id", users.PutUser),
		rest.Delete("/users/:id", users.DeleteUser),

		// user and book router
		rest.Get("/users/:id/books", users.GetUserAllBooks),

		// books router
		rest.Get("/books", books.GetAllBooks),
		rest.Post("/books", books.PostBook),
		rest.Get("/books/:id", books.GetBook),
		rest.Put("/books/:id", books.PutBook),
		rest.Delete("/books/:id", books.DeleteBook),
	)
	if err != nil {
		log.Fatal(err)
	}
	api.SetApp(router)
	log.Fatal(http.ListenAndServe(":8080", api.MakeHandler()))
}

type User struct {
	Id   string
	Name string
}

type Users struct {
	sync.RWMutex
	Store map[string]*User
}

type Book struct {
	Id     string
	UserID string
	Name   string
}

type Books struct {
	sync.RWMutex
	Store map[string]*Book
}

// ****************** User **********************

func (u *Users) GetAllUsers(w rest.ResponseWriter, r *rest.Request) {
	u.RLock()
	users := make([]User, len(u.Store))
	i := 0
	for _, user := range u.Store {
		users[i] = *user
		i++
	}
	u.RUnlock()
	w.WriteJson(&users)
}

func (u *Users) GetUser(w rest.ResponseWriter, r *rest.Request) {
	id := r.PathParam("id")
	u.RLock()
	var user *User
	if u.Store[id] != nil {
		user = &User{}
		*user = *u.Store[id]
	}
	u.RUnlock()
	if user == nil {
		rest.NotFound(w, r)
		return
	}
	w.WriteJson(user)
}

func (u *Users) GetUserAllBooks(w rest.ResponseWriter, r *rest.Request) {
	id := r.PathParam("id")
	u.RLock()
	var user *User
	if u.Store[id] != nil {
		user = &User{}
		*user = *u.Store[id]
	}
	u.RUnlock()
	if user == nil {
		rest.NotFound(w, r)
		return
	}
	w.WriteJson(user)
}

func (u *Users) PostUser(w rest.ResponseWriter, r *rest.Request) {
	user := User{}
	err := r.DecodeJsonPayload(&user)
	if err != nil {
		rest.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}
	u.Lock()
	id := fmt.Sprintf("%d", len(u.Store)) // stupid
	user.Id = id
	u.Store[id] = &user
	u.Unlock()
	w.WriteJson(&user)
}

func (u *Users) PutUser(w rest.ResponseWriter, r *rest.Request) {
	id := r.PathParam("id")
	u.Lock()
	if u.Store[id] == nil {
		rest.NotFound(w, r)
		u.Unlock()
		return
	}
	user := User{}
	err := r.DecodeJsonPayload(&user)
	if err != nil {
		rest.Error(w, err.Error(), http.StatusInternalServerError)
		u.Unlock()
		return
	}
	user.Id = id
	u.Store[id] = &user
	u.Unlock()
	w.WriteJson(&user)
}

func (u *Users) DeleteUser(w rest.ResponseWriter, r *rest.Request) {
	id := r.PathParam("id")
	u.Lock()
	delete(u.Store, id)
	u.Unlock()
	w.WriteHeader(http.StatusOK)
}

//************************* Books ************************

func (b *Books) GetAllBooks(w rest.ResponseWriter, r *rest.Request) {
	b.RLock()
	books := make([]Book, len(b.Store))
	i := 0
	for _, book := range b.Store {
		books[i] = *book
		i++
	}
	b.RUnlock()
	w.WriteJson(&books)
}

func (b *Books) GetBook(w rest.ResponseWriter, r *rest.Request) {
	id := r.PathParam("id")
	b.RLock()
	var book *Book
	if b.Store[id] != nil {
		book = &Book{}
		*book = *b.Store[id]
	}
	b.RUnlock()
	if user == nil {
		rest.NotFound(w, r)
		return
	}
	w.WriteJson(book)
}

func (b *Books) PostBook(w rest.ResponseWriter, r *rest.Request) {
	book := User{}
	err := r.DecodeJsonPayload(&book)
	if err != nil {
		rest.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}
	b.Lock()
	id := fmt.Sprintf("%d", len(b.Store)) // stupid
	book.Id = id
	b.Store[id] = &book
	b.Unlock()
	w.WriteJson(&book)
}

func (b *Books) PutBook(w rest.ResponseWriter, r *rest.Request) {
	id := r.PathParam("id")
	b.Lock()
	if b.Store[id] == nil {
		rest.NotFound(w, r)
		b.Unlock()
		return
	}
	book := Book{}
	err := r.DecodeJsonPayload(&book)
	if err != nil {
		rest.Error(w, err.Error(), http.StatusInternalServerError)
		b.Unlock()
		return
	}
	book.Id = id
	b.Store[id] = &book
	b.Unlock()
	w.WriteJson(&book)
}

func (b *Books) DeleteBook(w rest.ResponseWriter, r *rest.Request) {
	id := r.PathParam("id")
	b.Lock()
	delete(b.Store, id)
	b.Unlock()
	w.WriteHeader(http.StatusOK)
}
