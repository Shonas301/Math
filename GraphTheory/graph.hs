fold :: (a -> b -> b) ->
  b ->
  [a] ->
  b

unfold :: (b -> Maybe(a,b)) ->
  b ->
  [a]

unfoldG :: (Ord s) => (s -> (n, [(e,s)])) -> s -> (Vertex, LabGraph n e)
unfoldG f r = (r',res)
  where([r'], res) = unfoldGMany f [r]

unfoldGMany :: (Ord s) => (s->(n, [(e,s)]))->[s]->([Vertex], LabGraph n e)
unfoldGMany f roots = runSt(unfoldGManyST f roots)

graph :: LabGraph Int Char
  (_, graph) = unfoldG gen (0::Int)
  where gen x = (x,[('a', (x+1) `mod` 10), ('b', (x + 2) `mod` 10)])
