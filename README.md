# Class to use when building API views

- Pure Django Views
- APIView subclasses
- generics.\* subclasses
- viewsets.ModelViewSet

# When to use the above classes

- Use viewsets.ModelViewSet: - when you are going to allow all/most CRUD operations on a model
- Use generics.\* when you only want to allow some operations on a model
- Use APIView when you want to completely customize the behaviour.

## Access Controls Use Cases

- A user must be authenticated to access a poll or the list of polls.
- Only an authenticated users can create a poll.
- Only an authenticated user can create a choice.
- Authenticated users can create choices only for polls they have created.
- Authenticated users can delete only polls they have created.
- Only an authenticated user can vote. Users can vote for other people’s polls.

## Acces Control APIs

- API to create a user, we will call this endpoint /users/
- API to verify a user and get a token to identify them /login/

## Creating a user

- We will add an user serializer, which will allow creating in serializers.py.

## Authentication scheme setup

- With Django Rest Framework, we can set up a default authentication scheme which is applied to all views using DEFAULT_AUTHENTICATION_CLASSES.
- We will use the token authentication in the settings.py

## The login API

- We need an API where a user can give their username and password, and get a token back.
- We will not be adding a serializer, because we never save a token using this API.
- Add a view and connect it to urls.
