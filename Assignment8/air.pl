flight(mumbai, delhi, 5000, day, airindia).
flight(mumbai, pune, 3000, night, spicejet).
flight(mumbai, kolkata, 4000, day, goair).
flight(mumbai, jammu, 7000, night, indigo).
flight(mumbai, chennai, 6000, day, airindia).
flight(mumbai, jaipur, 4500, night, indigo).
flight(mumbai, kochi, 4500, night, indigo).
flight(mumbai, goa, 4500, night, indigo).
flight(mumbai, jammu, 8000, night, goair).
flight(mumbai, chennai, 6500, day, spicejet).
flight(mumbai, chandigarh, 4500, night, indigo).
flight(mumbai, nashik, 4500, night, indigo).


flight(delhi, mumbai, 4000, night, indigo).
flight(delhi, kolkata, 5000, day, airindia).
flight(delhi, chennai, 7000, night, spicejet).
flight(delhi, trichi, 4500, day, indigo).
flight(delhi, nagpur, 5000, day, spicejet).
flight(delhi, guwahati, 4000, day, airindia).
flight(delhi, nashik, 7600, night, spicejet).
flight(delhi, jalgaon, 4500, day, indigo).
flight(delhi, aurangabad, 5000, day, spicejet).
flight(delhi, chandigarh, 4000, day, airindia).

flight(kolkata, delhi, 5400, night, airindia).
flight(kolkata, nagpur, 6000, day, airindia).
flight(kolkata, jaipur, 5500, night, spicejet).
flight(kolkata, mumbai, 4500, day, spicejet).
flight(kolkata, pune, 3500, night, airindia).
flight(kolkata, kochi, 4000, day, spicejet).
flight(kolkata, goa, 5000, day, airindia).

flight(goa, delhi, 6000, day, spicejet).
flight(goa, kochi, 4500, night, airindia).
flight(goa, pune, 3500, day, goair).
flight(goa, mumbai, 5000, night, spicejet).
flight(goa, jaipur, 7500, day, airindia).
flight(goa, kochi, 6500, night, airasia).
flight(goa, kolkata, 5400, day, airindia).
flight(goa, nagpur, 5400, day, airindia).

flight(kochi, pune, 4300, day, spicejet).
flight(kochi, mumbai, 6500, night, airindia).
flight(kochi, nagpur, 5600, day, spicejet).
flight(kochi, goa, 6300, night, goair).
flight(kochi, jaipur, 7400, day, airindia).
flight(kochi, delhi, 7200, night, spicejet).

airport(kochi, op).
airport(pune, op).
airport(jaipur, op).
airport(nagpur, op).
airport(mumbai, op).
airport(delhi, op).
airport(aurangabad, nop).
airport(manali, nop).
airport(jalgaon, nop).
airport(nashik, nop).
airport(haidarabad, op).
airport(gudgaon, nop).
airport(chandigarh, nop).
airport(jammu, nop).
airport(kolkata, op).
airport(goa, op).


check_flight(X, Y) :- flight(X, Y, _, _, _).
day_flight_from(X) :- flight(X, A, _, day, B), format('Daytime flights from ~w fly to ~w with ~w.', [X, A, B]).
aff_from(X) :- flight(X, A, P, _, _), P < 5000, format('Affordable flights from ~w fly to ~w.', [X, A]).
airline_name(X, Y) :- flight(X, Y, _, _, A),
						format('~w is available from ~w to ~w. ~n', [A, X, Y]).

is_journey_possible(X, Y) :- flight(X, Y, _, _, _), airport(X, op), airport(Y, op), format('~w to ~w journey is possile. ~n', [X, Y]).


