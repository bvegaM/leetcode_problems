select p.FirstName,
    p.LastName,
    d.City,
    d.State
from Person p
left join Address  d on d.PersonId = p.PersonId