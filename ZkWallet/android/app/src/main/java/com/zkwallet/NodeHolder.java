package com.zkwallet;

import org.ethereum.geth.Account;
import org.ethereum.geth.Node;

public class NodeHolder {
    private Node node;
    private Account acc;
    private java.io.File filesDir;
    private static NodeHolder instance = null;

    private NodeHolder() {
    }

    public static NodeHolder getInstance() {
        if (instance == null) {
            instance = new NodeHolder();
        }
        return instance;
    }

    public Node getNode() {
        return node;
    }

    public void setNode(Node node) {
        this.node = node;
    }

    public Account getAcc() {
        return acc;
    }

    public void setAcc(Account acc) {
        this.acc = acc;
    }

    public java.io.File getFilesDir() {
        return filesDir;
    }

    public void setFilesDir(java.io.File filesDir) {
        this.filesDir = filesDir;
    }
}