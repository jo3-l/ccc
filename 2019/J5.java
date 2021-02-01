// This solution gets 7/15 points but TLEs on the other batches... any help would be appreciated.
import java.util.*;

public class J5 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        TrieNode rootNode = new TrieNode(false, null);
        for (int n = 0; n < 3; n++) {
            String[] parts = scanner.nextLine().split(" ");
            String originalString = parts[0];
            String replacementString = parts[1];

            Rule rule = new Rule(originalString, replacementString, n + 1); // Rule number is 1-based.

            TrieNode currentNode = rootNode;
            // Add this string to the trie.
            for (int i = 0; i < originalString.length(); i++) {
                TrieNode newNode = i == originalString.length() - 1
                        ? new TrieNode(true, new ArrayList<>(Collections.singletonList(rule))) // Last character
                        : new TrieNode(false, null);

                // Connect this node to the last one, and then set the new node to the current node.
                currentNode = currentNode.connect(originalString.charAt(i), newNode);
            }
        }

        String[] parts = scanner.nextLine().split(" ");
        int stepsToTake = Integer.parseInt(parts[0]);
        String originalString = parts[1];
        String finalString = parts[2];

        SequenceFinder finder = new SequenceFinder(stepsToTake, finalString, rootNode);
        List<RuleMatch> history = finder.getRuleHistory(originalString);
        if (history == null) {
            System.out.println("Didn't find a sequence of substitutions that matched the given criteria. This should never happen!");
            return;
        }

        for (RuleMatch match : history) System.out.println(match.toString());
    }

    private static class SequenceFinder {
        private final int stepsToTake;
        private final String finalString;
        private final TrieNode rootNode;
        private final List<RuleMatch> history = new ArrayList<>();

        public SequenceFinder(int stepsToTake, String finalString, TrieNode rootNode) {
            this.stepsToTake = stepsToTake;
            this.finalString = finalString;
            this.rootNode = rootNode;
        }

        public List<RuleMatch> getRuleHistory(String str) {
            // Edge cases
            int stepsTaken = history.size();
            if (str.equals(finalString) && stepsTaken == stepsToTake) return history;
            if (stepsTaken >= stepsToTake) return null;

            // List of nodes that are in the middle of being matched currently
            LinkedList<TrieNode> matchingNodes = new LinkedList<>();

            // Loop over the string and run a depth-first recursive search over possible substitutions we can perform
            for (int i = 0; i < str.length(); i++) {
                char c = str.charAt(i);
                int startIteratingAt = 0;

                // See if there's a substitution rule that starts with the current character
                TrieNode adjacentNode = rootNode.getAdjacentNode(c);
                if (adjacentNode != null) {
                    // If there are rules on this node, then apply them to the current string and recursively find rules which can be applied to that new string
                    for (Rule rule : adjacentNode.applicableRules) {
                        RuleMatch ruleMatch = createRuleMatch(rule, str, i);
                        // Add this match to the history
                        history.add(ruleMatch);
                        // See if we can obtain a valid result using the new string
                        List<RuleMatch> resultingHistory = getRuleHistory(ruleMatch.resultingString);
                        // If we didn't get a valid result, remove the match from the history
                        if (resultingHistory == null) history.remove(history.size() - 1);
                            // If we did get a valid result, bubble it upwards
                        else return history;
                    }

                    if (!adjacentNode.isLeaf()) {
                        matchingNodes.addFirst(adjacentNode);
                        startIteratingAt = 1; // Skip iterating over the node we just added.
                    }
                }

                // Now continue matching the nodes from previous iterations
                ListIterator<TrieNode> iter = matchingNodes.listIterator(startIteratingAt);
                while (iter.hasNext()) {
                    TrieNode node = iter.next();
                    adjacentNode = node.getAdjacentNode(c);
                    if (adjacentNode != null) {
                        // Similar steps as that above
                        for (Rule rule : adjacentNode.applicableRules) {
                            RuleMatch ruleMatch = createRuleMatch(rule, str, i);
                            history.add(ruleMatch);
                            List<RuleMatch> resultingHistory = getRuleHistory(ruleMatch.resultingString);
                            if (resultingHistory == null) history.remove(history.size() - 1);
                            else return history;
                        }

                        if (adjacentNode.isLeaf()) iter.remove(); // Done with this node for now, so remove it.
                        else iter.set(adjacentNode); // Otherwise, set it to the adjacent node (advancing 1 position).
                    } else {
                        iter.remove(); // Unable to find an adjacent node, so remove it.
                    }
                }
            }

            return null;
        }

        private RuleMatch createRuleMatch(Rule rule, String str, int endIndex) {
            int startIndex = endIndex - rule.originalString.length() + 1;
            return new RuleMatch(rule, str, startIndex);
        }
    }

    private static class RuleMatch {
        private final String resultingString;
        private final int startPosition;
        private final int ruleNumber;

        public RuleMatch(Rule rule, String originalString, int startIndex) {
            this.resultingString = rule.applyTo(originalString, startIndex);
            this.startPosition = startIndex + 1; // Question asks for the position to be 1-based.
            this.ruleNumber = rule.ruleNumber;
        }

        @Override
        public String toString() {
            return ruleNumber + " " + startPosition + " " + resultingString;
        }
    }

    private static class Rule {
        public final String originalString;
        public final String replacementString;
        public final int ruleNumber;

        public Rule(String originalString, String replacementString, int ruleNumber) {
            this.originalString = originalString;
            this.replacementString = replacementString;
            this.ruleNumber = ruleNumber;
        }

        public String applyTo(String str, int startIndex) {
            String startSubstr = str.substring(0, startIndex);
            String endSubstr = str.substring(startIndex + originalString.length());
            return startSubstr + replacementString + endSubstr;
        }
    }

    private static class TrieNode {
        public final boolean hasRule;
        public final List<Rule> applicableRules;
        private final Map<Character, TrieNode> adjacentNodes = new HashMap<>();

        public TrieNode(boolean hasRule, List<Rule> rules) {
            this.applicableRules = rules == null ? new ArrayList<>() : rules;
            this.hasRule = hasRule;
        }

        public TrieNode connect(char c, TrieNode node) {
            return adjacentNodes.merge(c, node, (oldNode, __) -> {
                // Merge the old node's applicable rules with the new node's.
                TrieNode newNode = new TrieNode(oldNode.hasRule || node.hasRule, oldNode.applicableRules);
                newNode.applicableRules.addAll(node.applicableRules);

                // Merge the old node's adjacent nodes with the new node's.
                newNode.adjacentNodes.putAll(oldNode.adjacentNodes);
                for (Map.Entry<Character, TrieNode> entry : node.adjacentNodes.entrySet())
                    newNode.connect(entry.getKey(), entry.getValue());

                return newNode;
            });
        }

        public TrieNode getAdjacentNode(char c) {
            return adjacentNodes.get(c);
        }

        public boolean isLeaf() {
            return hasRule && adjacentNodes.isEmpty();
        }
    }
}
