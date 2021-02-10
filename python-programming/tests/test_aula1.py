import mock
import listProcessing
import tuplesProcessing
import functionsReturningNone

#Exercicio 1.1
@mock.patch('listProcessing.size', side_effect = listProcessing.size)
def test_size(mock_size):
    assert mock_size([1,2,3,4]) == 4
    assert mock_size.call_count == 5 

#Exercicio 1.2
@mock.patch('listProcessing.numberSum', side_effect = listProcessing.numberSum)
def test_numberSum(mock_numberSum):
    assert mock_numberSum([1,2,3,4]) == 10
    assert mock_numberSum.call_count == 5

#Exercicio 1.3
@mock.patch('listProcessing.exists', side_effect = listProcessing.exists)
def test_exists(mock_exists):
    assert mock_exists([1,2,3,4], 5) == False
    assert mock_exists.call_count == 5
    mock_exists.call_count = 0
    assert mock_exists([1,2,3,4], 2) == True
    assert mock_exists.call_count == 2

#Exercicio 1.4
@mock.patch('listProcessing.concatenation', side_effect = listProcessing.concatenation)
def concatenation(mock_concatenation):
    assert mock_concatenation([1,2,3,4], [5,6]) == [1,2,3,4,5,6]
    assert mock_concatenation.call_count == 3

#Exercicio 1.5
@mock.patch('listProcessing.reverse', side_effect = listProcessing.reverse)
def test_reverse(mock_reverse):
    assert mock_reverse([1,2,3,4]) == [4,3,2,1]
    assert mock_reverse.call_count == 5

#Exercicio 1.6
@mock.patch('listProcessing.isPalindrome', side_effect = listProcessing.isPalindrome)
def test_isPalindrome(mock_isPalindrome):
    assert mock_isPalindrome([3,2,3])
    assert mock_isPalindrome([3,2,2,3])
    assert not mock_isPalindrome([1,2,3])
    assert mock_isPalindrome.call_count == 7

#Exercicio 1.7
@mock.patch('listProcessing.multipleConcatenation', side_effect = listProcessing.multipleConcatenation)
def test_multipleConcatenation(mock_multipleConcatenation):
    assert mock_multipleConcatenation([[1,2], [3,4]]) == [1,2,3,4]
    assert mock_multipleConcatenation([[1,2], [3,4], [5]]) == [1,2,3,4,5]

#Exercicio 1.8
@mock.patch('listProcessing.replace', side_effect = listProcessing.replace)
def test_replace(mock_replace):
    assert mock_replace([1,2,3,4], 3, 5) == [1,2,5,4]
    assert mock_replace([1,2,3,4], 5, 6) == [1,2,3,4]

#Exercicio 1.9
@mock.patch('listProcessing.orderedMerge', side_effect = listProcessing.orderedMerge)
def test_orderedMerge(mock_orderedMerge):
    assert mock_orderedMerge([1,2,3,4], [2,3,4,5]) == [1,2,2,3,3,4,4,5] 

#Exercicio 2.1
@mock.patch('tuplesProcessing.splitting', side_effect = tuplesProcessing.splitting)
def test_splitting(mock_splitting):
    assert mock_splitting([(1, 'a'), (2, 'b'), (3, 'c')]) == ([1,2,3], ['a','b','c'])
    assert mock_splitting.call_count == 4

#Exercicio 3.3
@mock.patch('functionsReturningNone.ranking', side_effect = functionsReturningNone.ranking)
def test_ranking(mock_ranking):
    assert mock_ranking(([1,2,3], ['a','b','c'])) == [(1, 'a'), (2, 'b'), (3, 'c')]
    assert mock_ranking.call_count == 4
    assert mock_ranking(([1,2,3], ['a','b','c','d'])) == None
    assert mock_ranking.call_count == 5

#Exercicio 3.4
@mock.patch('functionsReturningNone.lowest', side_effect = functionsReturningNone.lowest)
def test_lowest(mock_lowest):
    assert mock_lowest([1,2,3,0,5]) == 0
    assert mock_lowest.call_count == 6
    assert mock_lowest([]) == None
