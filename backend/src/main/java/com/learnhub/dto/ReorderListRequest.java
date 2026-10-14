package com.learnhub.dto;

import jakarta.validation.Valid;

import java.util.ArrayList;
import java.util.List;

/**
 * Request payload containing the list of ordered items or IDs for reordering modules and lessons.
 */
public class ReorderListRequest {

    @Valid
    private List<ReorderItemRequest> items = new ArrayList<>();

    private List<Long> orderedIds = new ArrayList<>();

    public ReorderListRequest() {
    }

    public ReorderListRequest(List<ReorderItemRequest> items) {
        this.items = items;
    }

    public List<ReorderItemRequest> getItems() {
        return items;
    }

    public void setItems(List<ReorderItemRequest> items) {
        this.items = items;
    }

    public List<Long> getOrderedIds() {
        if (orderedIds != null && !orderedIds.isEmpty()) {
            return orderedIds;
        }
        if (items != null && !items.isEmpty()) {
            List<Long> ids = new ArrayList<>();
            for (ReorderItemRequest item : items) {
                if (item != null && item.getId() != null) {
                    ids.add(item.getId());
                }
            }
            return ids;
        }
        return new ArrayList<>();
    }

    public void setOrderedIds(List<Long> orderedIds) {
        this.orderedIds = orderedIds;
    }
}
